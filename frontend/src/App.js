import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';

// TODO: Import components for different pages

function App() {
  return (
    <Router>
      <div className="App">
        {/* TODO: Implement navigation/header component */}
        <main>
          <Switch>
            {/* TODO: Define routes for different pages */}
            <Route exact path="/" render={() => <div>EventConnect Home Page</div>} />
          </Switch>
        </main>
        {/* TODO: Implement footer component */}
      </div>
    </Router>
  );
}

export default App;