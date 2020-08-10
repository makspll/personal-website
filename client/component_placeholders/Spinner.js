import React from 'react';

class Spinner extends React.Component{
    
    render(){
        return (<div className="d-flex flex-column flex-grow-1 justify-content-center align-items-center ">
                        <div className="spinner-grow  text-warning" role="status">
                            <span className="sr-only">Loading... </span>
                        </div>
                </div>);
    }
}

export default Spinner;