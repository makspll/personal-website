import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"
import ProjectBlock from "./ProjectBlock.js";
import TagFilterNav from "./TagFilterNav.js";


class ProjectListingBlock extends React.Component{
    constructor(props){
        super(props);

        this.state = {
            selected_tags : [],
        }
    }

    set_selected_tags(tags){

        this.setState({
            selected_tags: tags,
        })
    }

    render() { 
        const  {isLoaded, json} = this.props;
        
        let content = null

        // place either skeleton or loaded content
        if(isLoaded){
            // map each project json block value to a project component
            let project_blocks = json.value.project_items.map((value,index)=>

                <ProjectBlock 
                    key={index} 
                    isLoaded={true} 
                    json={value} 
                    filters={{selected_tags:this.state.selected_tags}}/>
            )
            let heading = (json.value.heading)? 
                            <h3 className="project-listing-heading h1 my-2">{json.value.heading}</h3> : 
                            null;

            content =
                <React.Fragment>
                    {heading}
                    <hr/>
                    <TagFilterNav set_selected_tags_handler={(tags)=>this.set_selected_tags(tags)} selected_tags={this.state.selected_tags}/>
                    {project_blocks}
                </React.Fragment>;

         } else {
            // create random placeholders
            let numrows = 10;
            var rows = [];
            for (var i = 0; i < numrows; i++) {
                if( i+1 < numrows){
                    rows.push(
                            [<ProjectBlock key={i}/>,
                            <div key={-(i - 1)} className="my-2"></div>]
                        );
                }
                else {
                    rows.push(
                        <ProjectBlock key={i}/>
                    )
                }
            }

            content = rows;
        }

       

        return (
                <div className="project-listing list-unstyled p-2 border ">
                    {content}
                </div>
        )
    }

}

export default ProjectListingBlock
