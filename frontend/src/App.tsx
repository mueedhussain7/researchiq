import { BrowserRouter, Routes, Route } from 'react-router-dom'

const modules = [
  'Impact Assessment',
  'Citation Validation',
  'Gap Detection',
  'Innovation Discovery',
]

function Home() {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="text-center max-w-lg px-4">
        <h1 className="text-4xl font-bold text-brand-700 mb-3">ResearchIQ</h1>
        <p className="text-gray-500 text-lg mb-8">
          AI-Powered Research Intelligence Platform
        </p>
        <div className="grid grid-cols-2 gap-3">
          {modules.map((m) => (
            <div
              key={m}
              className="bg-white border border-gray-200 rounded-lg p-4 text-gray-700 text-sm font-medium"
            >
              {m}
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
  )
}
