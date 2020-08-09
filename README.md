# Personal Website

## features
- Wagtail CMS
- Blog Posts
- Project Portfolio
- Document Display

## setup 
add a `.env` file in root directory with the following inside:
```
DJANGO_ENV={{ dev/prod }}
DJANGO_SECRET_KEY={{ secret key}}
DROPBOX_OAUTH2_TOKEN={{ dropbox oauth2 key }}
```
 
install npm dependencies from package.json and python dependencies from requirements.txt

## heroku
the project is ready to be deployed on heroku since it contains a procfile and a post_compile hook, just link up your repo to heroku, set the config vars above and deploy.