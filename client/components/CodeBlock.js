
import React from 'react';
import Prism from 'prismjs';
import PrismCode from 'react-prism';

class CodeBlock extends React.Component{
    
    render(){
        let {isLoaded, json} = this.props;

        let content = null;
        if(isLoaded){
            content = <PrismCode component="pre" className={`language-${json.value.language} code-toolbar`}>
                        {json.value.code}
                        </PrismCode>
        }else{
            
        }
        return content;
    }
} 

export default CodeBlock;