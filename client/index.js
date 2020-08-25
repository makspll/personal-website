import FreeformListingBlock from './components/FreeformListingBlock';
import ArticleListingBlock from './components/ArticleListingBlock';
import React from 'react';
import ReactDOM from 'react-dom';
import './css/all.scss';
import AOS from 'aos';
import './js/common.js';
import 'popper.js';
import Prism from 'prismjs';
import 'bootstrap';
import Rellax from 'rellax';
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

console.log("asd",rellax);
console.log("hello");
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
