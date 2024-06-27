import React from 'react';
import Header from './components/Header';
import Card from './components/Card';
import PredictionTool from './components/PredictionTool';
// import FeedbackForm from './components/FeedbackForm';
import './App.css'; // Import your styles
let problem = "Parkinson's disease detection lacks efficient,"+
" accessible methods, hindering early intervention crucial for symptom management and quality of life."
let vision = "Develop a robust machine learning model leveraging neurological data to accurately predict" +
" Parkinson's disease presence, aiding in timely diagnosis and treatment"
let conclusion = "By harnessing advanced technology, we aim to improve early detection rates, enhancing "+ 
"patient outcomes and quality of life for individuals at risk of Parkinson's disease"
const App = () => {
  return (
    <div>
      <Header />
      <div className="home-section" >
        <Card title="Problem" num={1} content={problem} />
        <Card title="Vision" num={2} content={vision} />
        <Card title="Conclusion" num={3} content={conclusion}  />
      </div>
      <PredictionTool />
      {/* <FeedbackForm /> */}
      <footer>
        <div className="footer">
          <p>&copy; 2024 NeuroPredict. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default App;
