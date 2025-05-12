import ChatWindow from './components/ChatWindows';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navigate } from "react-router-dom";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/chat" element={<ChatWindow />} />
        <Route path="/" element={<Navigate to="/chat" replace />} />
      </Routes>
    </Router>
  );
}

export default App;