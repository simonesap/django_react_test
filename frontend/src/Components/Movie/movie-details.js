import React from 'react'

function MovieDetails(props){

    return (
        <div>
            { props.movie ? (
                <div>
                    <h1>{props.movie.title}</h1>
                    <p>{props.movie.description}</p>
                    <p>Voti: {props.movie.number_of_ratings}</p>
                    <p>Media: {props.movie.avg_rating}</p>
                </div>
            ) : null}
        </div>
    )
}

export default MovieDetails;