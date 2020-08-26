
import FreeformListingBlock from './components/FreeformListingBlock';
import ArticleListingBlock from './components/ArticleListingBlock';
import React from 'react';
import ReactDOM from 'react-dom';
import AOS from 'aos';
import Prism from 'prismjs';
import Rellax from 'rellax';
import 'popper.js';
import 'bootstrap';

import './css/all.scss';
import './js/common.js';

var images = document.getElementsByClassName('img-background');

var rellax = new Rellax('.rellax', {
    speed: -2,
    center: false,
    wrapper: null,
    round: true,
    vertical: true,
    horizontal: false,
    breakpoints:[480,768,1200]

  });


let freeform_content_root = document.getElementById('freeform_content');
if (freeform_content_root){
    ReactDOM.render(
        <FreeformListingBlock />,
            freeform_content_root
        );
    
}

let article_listing_root = document.getElementById('article_listing')

if(article_listing_root){
    ReactDOM.render(
        <ArticleListingBlock />,
        article_listing_root
        );
}

    
Prism.highlightAll();
AOS.init();

document.addEventListener('DOMContentLoaded', (event) => {

});
