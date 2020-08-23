import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"
import ProjectBlock from "./ProjectBlock.js";
import FiltersNav from "./FiltersNav.js";
import {initial_filters} from "../components/FiltersNav";

import Spinner from "../component_placeholders/Spinner";
import TagFilter from "../components/TagFilter";
import CheckboxFilter from "../components/CheckboxFilter";

class ProjectListingBlock extends React.Component{
    constructor(props){
        super(props);

        this.state = {
            filters: initial_filters,
        }
    }

    set_filters_handler(new_filters){
        this.setState({
            filters:new_filters,
        })
    }

    render() { 
        const  {isLoaded, json} = this.props;
        let {filters} = this.state;

        let content = null

        // place either skeleton or loaded content
        if(isLoaded){
            // map each project json block value to a project component
            let project_blocks = json.value.project_items.map((value,index)=>

                <ProjectBlock 
                    key={index} 
                    isLoaded={true} 
                    json={value} 
                    filters={filters}/>
            )
            let heading = (json.value.heading)? 
                            <h3 className="project-listing-heading h1 my-2">{json.value.heading}</h3> : 
                            null;

            content =
                <React.Fragment>
                    {heading}
                    {(heading)?<hr/>:null}
                    {/*  set_selected_tags_handler={(tags)=>this.set_selected_tags(tags)} selected_tags={this.state.selected_tags} */}
                    <FiltersNav filters={this.state.filters} set_filters={(new_filters)=>this.set_filters_handler(new_filters)}>
                        <TagFilter/>
                        <CheckboxFilter button_names={["Hide coursework"]}/>
                    </FiltersNav>
                    {project_blocks}
                </React.Fragment>;

         } else {
            
            content = <Spinner/>;
        }

        return (
                <div className="project-listing list-unstyled p-2 border ">
                    {content}
                </div>
        )
    }

}

export default ProjectListingBlock
