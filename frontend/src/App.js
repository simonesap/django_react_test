import React, {useState, useEffect, Component } from 'react';
import './App.css';
import MovieList from './Components/Movie/movie-list.js';
import MovieDetails from './Components/Movie/movie-details.js';

function App() {

  // useState permette di usare lo stato React e recuperare dal Component
  // movie-list.js la funzione al suo interno, infatti movie-list.js
  // è anche chiamato un componente funzione 
  const [movies, setMovie] = useState([]);

  // Recupero il dettaglio del film cliccato 
  const [selectedMovie, setSelectedMovie] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/movies/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token d6c4dffe6b74485df54ada90a4a1fe387af117a5'
      }
    })
    .then( resp => resp.json())
    .then( resp => setMovie( resp))
    .catch( error => console.log(error))
  }, []);

  const movieClicked = movie => {
    setSelectedMovie(movie);
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>TEST-APP</h1>
      </header>
      <div className='layout'>
        <div>Lista film</div>
          <MovieList movies={movies} movieClicked={movieClicked}/>
          <MovieDetails movie={selectedMovie}/>
      </div>
    </div>
  );
}

export default App;
