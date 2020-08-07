import React from 'react';
import ReactDOM from 'react-dom';

class ProjectBlock extends React.Component{
    render() { return(
        <li className="project-listing-project p-3 border position-relative">
            
            <div className="project-listing-project-body">
                <h4 className="h2 mb-0"></h4>
                <div className="text-muted h6">
                    <span><i className="fa fa-hourglass-start fa-sm" aria-hidden="true"></i></span>
                    <span></span>
                    <span><i className="fa fa-hourglass-end fa-sm" aria-hidden="true"></i></span>
                    <span></span>
                    <br/>
                   
                </div>

                <p></p>
                <a href="{% pageurl value.project_page %}" className="stretched-link"></a>
                <div className="overlay">Read More</div>
            </div>
        </li>
    )}

}

for(const element of document.getElementsByClassName('project_block')){
    ReactDOM.render(
        <ProjectBlock />,
        element
      );
}
