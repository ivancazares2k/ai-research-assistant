import { useState } from "react"
import ReactMarkdown from "react-markdown"
import "./App.css"

function App() {
  const [topic, setTopic] = useState("")
  const [report, setReport] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleResearch = async () => {
    if (!topic.trim()) return
    setLoading(true)
    setError(null)
    setReport(null)

    try {
      const response = await fetch("http://localhost:8000/research", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic })
      })
      const data = await response.json()
      setReport(data)
    } catch (err) {
      setError("Something went wrong. Is the backend running?")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      {!report && !loading && (
        <div className="hero">
          <h1>AI Research Assistant</h1>
          <p className="subtitle">Type any topic and three AI agents will research it for you</p>
          <div className="input-row">
            <input
              type="text"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleResearch()}
              placeholder="e.g. quantum computing, climate change, stoicism..."
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