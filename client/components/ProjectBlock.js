import React from 'react';
import {GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"
import { LazyLoadImage } from 'react-lazy-load-image-component';

const ProjectBlockLoader = (props) => (
  <ContentLoader 
    speed={2}
    height="250"
    viewBox="0 0 250 100 "
    backgroundColor="#f3f3f3"
    foregroundColor="#ecebeb"
    style={{ width: '100%' , textAlign: 'left'}}
    className="project-listing-project p-3 border position-relative"
    preserveAspectRatio="none"
    {...props}
  >
    <rect x="7" y="2" rx="0" ry="0" width="85" height="93" /> 
    <rect x="106" y="9" rx="0" ry="0" width="170" height="17" /> 
    <rect x="106" y="37" rx="0" ry="0" width="113" height="6" /> 
    <rect x="106" y="55" rx="0" ry="0" width="87" height="6" /> 
    <rect x="106" y="71" rx="0" ry="0" width="87" height="6" /> 
    <rect x="106" y="86" rx="0" ry="0" width="87" height="6" />
  </ContentLoader>
)


class ProjectBlock extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            project_page_loaded: false,
            project_page_json: null,
        }
    }

    load_project_page(){
        var url_href = GET_API_ROOT_URL() + `pages/${this.props.json.project_page}/`;

        fetch(url_href).then(res => res.json())
            .then( 
                (result) =>{
                    this.setState({
                        isLoaded: true,
                        project_page_json: result,
                        project_page_loaded: true,
                    });
                },
                (error)=>{
                    console.error(error);
                }
            )
    }

    componentDidMount() {
        if(this.props.isLoaded){
            this.load_project_page()
        }
    }
    componentDidUpdate(prevProps, prevState, snapshot){
        // on after content loaded
        // we find project page and update state
        if(!prevProps.isLoaded && this.props.isLoaded === true){
            // find which page we're attached to 
            this.load_project_page();
        }
    }


    render() {
        
        let {isLoaded,json,filters} = this.props;

        
        let content = null;
        if (isLoaded && this.state.project_page_loaded){

            // check we pass filters first
            let has_some_selected_tag = 
                filters.selected_tags.length === 0 || 
                filters.selected_tags.some((filter_tag)=>
                    this.state.project_page_json.tags.includes(filter_tag)
                );

            // end early
            if (!has_some_selected_tag){
                return null
            }

            let image_title = this.state.project_page_json.featured_image.title;
            let thumbnail_json = this.state.project_page_json.featured_image_thumbnail;
            let placeholder_img_json = this.state.project_page_json.featured_image_placeholder;

            let image = 
                    <LazyLoadImage
                        alt={image_title}
                        src={thumbnail_json.url}
                        height={thumbnail_json.height}
                        width={thumbnail_json.width}
                        className="rounded align-self-center img-fluid"
                    />

            let tags = this.state.project_page_json.tags.map((value,index)=>{
                <span key={index} className="badge badge-secondary mt-2"> { value } </span>
            })

            content =  
                <li className="project-listing-project p-3 border position-relative">
                    {image}
                    <div className="project-listing-project-body">
                        <h4 className="h2 mb-0">{(this.props.json.override_title) ? 
                                                    this.props.json.override_title :
                                                    this.state.project_page_json.title}</h4>
                        <div className="text-muted h6">
                            <span><i className="fa fa-hourglass-start fa-sm" aria-hidden="true"></i></span>
                            <span> {(this.state.project_page_json.project_start_date)? 
                                        this.state.project_page_json.project_start_date :
                                        "Not Started"} -
                            </span>
                            <span> <i className="fa fa-hourglass-end fa-sm" aria-hidden="true"></i></span>
                            <span> {(this.state.project_page_json.project_end_date)? 
                                        this.state.project_page_json.project_end_date :
                                        "Not Completed"}</span>
                            <br/>
                            {tags}
                        </div>

                            <p dangerouslySetInnerHTML={ {__html:this.state.project_page_json.blurb}}></p>
                        <a href={ this.state.project_page_json.meta.html_url.toString() } className="stretched-link"></a>
                        <div className="overlay">Read More</div>
                    </div>
                </li>
        }
        else{
            content = <ProjectBlockLoader/>
        }

        return(content)
    }

}

export default ProjectBlock