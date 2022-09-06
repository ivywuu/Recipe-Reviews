import './App.css';
import React from "react";
import {
  Routes, 
  Route,
} from "react-router-dom";
import Header from './components/Header';

import RecipePage from './pages/RecipePage'
import Home from './pages/Home';
import Tools from './pages/Tools';
import Pantry from './pages/Pantry';
import RecipeRec from './pages/RecipeRec';
import AddRecipe from './pages/AddRecipe';

function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="tools" element={<Tools />} />
        <Route path="pantry" element={<Pantry />} />
        <Route path="recipe-recommendations" element={<RecipeRec />} />
        <Route path="recipe-reviews" element={<RecipePage />} />
      </Routes>

    </div>
  );
}

export default App;
