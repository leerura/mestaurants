import './App.css';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import RegisterForm from './componets/RegisterForm';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/register" element={<RegisterForm />} /> 
      </Routes>
    </Router>
    
    
  );
}

export default App;
