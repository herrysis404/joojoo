import React from 'react';
import { Calendar } from './Calendar';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
        <Route path='/' exact={true} component={Calendar}/>
    </Router>
  );
}

export default App;
