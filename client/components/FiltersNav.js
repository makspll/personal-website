import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"

export let initial_filters = {
    selected_tags:[],
    selected_radiobuttons:[],
}

class FiltersNav extends React.Component{
    

    set_filters_handler(new_filters){

        this.props.set_filters(new_filters);
    }

    render() { 

 
        let child_count = React.Children.count(this.props.children);
        let counter = 0;

        let childrenWithProps = React.Children.map(this.props.children, child => {
            counter = counter + 1;
            const props = { filters:this.props.filters, set_filters:(new_filters)=>this.set_filters_handler(new_filters) };
            let child_jsx = child;
            if (React.isValidElement(child)) {
                child_jsx= React.cloneElement(child, props);
            }
            return <React.Fragment key={child_count}>{counter != 1?<hr/>:null}{child_jsx}</React.Fragment>;
        });

        let content = 
            <nav className="bg-primary text-light border border-gray p-2 overflow-auto">
                <div className="d-flex">
                    <p className="m-0 text-left h3">Filters</p>

                    <button 
                        className="btn btn-warning btn-sm ml-auto"
                        onClick={()=>this.props.set_filters(initial_filters)}
                        >
                        Clear Filters
                    </button>

                </div>
                <hr className="my-2 bg-light"/>
                {childrenWithProps}
            </nav>

        return(content);    
}

}

export default FiltersNav
