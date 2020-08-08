import React from 'react';
import {GET_ROOT_URL,GET_API_ROOT_URL} from '../DynamicVariables.js';
import ContentLoader from "react-content-loader"

class TagFilterNav extends React.Component{

    render() { 
        return(
            <nav className="bg-primary text-light border border-gray p-2">
                <h3 className="m-0 text-left">Filters</h3>
                <hr className="my-1 bg-light"/>

            </nav>
        )    
}

}

export default TagFilterNav
