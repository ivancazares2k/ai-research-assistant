import { useState } from "react"
import ReactMarkdown from "react-markdown"
import "./App.css"

function App() {
  const [accessCode, setAccessCode] = useState("")
  const [authenticated, setAuthenticated] = useState(false)
  const [authError, setAuthError] = useState("")
  const [topic, setTopic] = useState("")
  const [report, setReport] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleAuth = async () => {
    try {
      const response = await fetch("https://ai-research-assistant-production-093d.up.railway.app/validate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: accessCode })
      })
      if (response.ok) {
        setAuthenticated(true)
        setAuthError("")
      } else {
        setAuthError("Invalid access code. Please try again.")
      }
    } catch {
      setAuthError("Could not reach server.")
    }
  }

  const handleResearch = async () => {
    if (!topic.trim()) return
    setLoading(true)
    setError(null)
    setReport(null)

    try {
      const response = await fetch("https://ai-research-assistant-production-093d.up.railway.app/research", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Access-Code": accessCode
        },
        body: JSON.stringify({ topic })
      })
      if (response.status === 429) {
        setError("Rate limit reached. You can make 10 requests per hour.")
        return
      }
      const data = await response.json()
      setReport(data)
    } catch {
      setError("Something went wrong. Is the backend running?")
    } finally {
      setLoading(false)
    }
  }

  if (!authenticated) {
    return (
      <div className="auth-screen">
        <div className="auth-box">
          <h1>AI Research Assistant</h1>
          <p className="auth-sub">Enter your access code to continue</p>
          <input
            type="text"
            value={accessCode}
            onChange={(e) => setAccessCode(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleAuth()}
            placeholder="Access code"
            className="auth-input"
          />
          <button onClick={handleAuth} className="auth-btn">
            Enter
          </button>
          {authError && <p className="error">{authError}</p>}
        </div>
      </div>
    )
  }

  return (
    <div className="container">
      {!report && !loading && (
        <div className="hero">
          <h1>AI Research Assistant</h1>
          <p className="subtitle">Three AI agents research any topic in parallel</p>
          <div className="input-row">
            <input
              type="text"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleResearch()}
              placeholder="e.g. quantum computing, stoicism, climate change..."
              className="topic-input"
            />
            <button onClick={handleResearch} className="research-btn">
              Research
            </button>
          </div>
          {error && <p className="error">{error}</p>}
        </div>
      )}

      {loading && (
        <div className="loading">
          <div className="spinner" />
          <p>Three agents are researching <strong>{topic}</strong>...</p>
          <p className="loading-sub">This takes 20-30 seconds</p>
        </div>
      )}

      {report && (
        <div className="report">
          <button className="back-btn" onClick={() => { setReport(null); setTopic("") }}>
            ← New Research
          </button>
          <h1>{report.topic}</h1>

          <div className="section">
            <h2>📋 Report</h2>
            <div className="content"><ReactMarkdown>{report.report}</ReactMarkdown></div>
          </div>

          <div className="section">
            <h2>🔍 Search Findings</h2>
            <div className="content"><ReactMarkdown>{report.search}</ReactMarkdown></div>
          </div>

          <div className="section">
            <h2>🧠 Analysis</h2>
            <div className="content"><ReactMarkdown>{report.analysis}</ReactMarkdown></div>
          </div>
        </div>
      )}
    </div>
  )
}

export default App