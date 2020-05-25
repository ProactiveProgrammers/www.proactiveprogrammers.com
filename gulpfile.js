/* eslint-disable block-scoped-var */

// Gulp {{{

// use gulp to manage the web site
var gulp = require('gulp');

// }}}

// Package Loading {{{

// declare variables for used packages
var browserSync = require('browser-sync').create();
var del = require('del');
var argv = require('yargs').argv;
var spawn = require('child_process').spawn;

// }}}

// Reloading of gulpfile.js {{{

// Usage: gulp auto-reload --task deploy-watch

gulp.task('auto-reload', function() {
  var p;
  gulp.watch('gulpfile.js', spawnChildren);
  spawnChildren();
  function spawnChildren(e) {
    // kill previous spawned process
    if(p) { p.kill(); }
    // `spawn` a child `gulp` process linked to the parent `stdio`
    p = spawn('gulp', [argv.task], {stdio: 'inherit'});
  }
});

// }}}

// Variables {{{

// define the directories for the fonts
var SITE_HTML_SOURCE = '**/*.html';
var SITE_HTML_DEST = '_site/';

// define the directories for the fonts
var SITE_CSS_SOURCE = 'css/*.css';
var SITE_CSS_DEST = '_site/css';

// define the directories for the fullpage.js javascript files
var FULLPAGE_JAVASCRIPT_SOURCE = ['node_modules/fullpage.js/dist/fullpage.min.js', 'node_modules/fullpage.js/dist/fullpage.min.js.map'];
var FULLPAGE_JAVASCRIPT_DEST = '_site/js';

// define the directories for the fullpage.js javascript files
var FULLPAGE_CSS_SOURCE = ['node_modules/fullpage.js/dist/fullpage.min.css', 'node_modules/fullpage.js/dist/fullpage.min.css.map'];
var FULLPAGE_CSS_DEST = '_site/css';

// }}}

// Browser {{{

// TASK: use browsersync to load the site for local synced testing
gulp.task('browsersync', function() {
  browserSync.init({
    server: {
      baseDir: '_site/',
    },
    open: false,
  });
  gulp.watch(['_site/**/*.html', '_site/**/*.css', '_site/**/*.js']).on('change', browserSync.reload);
});

// }}}

// Maintenance {{{

// TASK: delete the generated site
gulp.task('clean', function() {
  return del([
    '_site/**/*',
  ]);
});

// }}}

// Deploy {{{

// TASK: Copy all of the HTML for the site to the destination directory
gulp.task('html-site', function() {
  return gulp.src(SITE_HTML_SOURCE)
    .pipe(gulp.dest(SITE_HTML_DEST));
});

// TASK: Copy all of the CSS for the site to the destination directory
gulp.task('css-site', function() {
  return gulp.src(SITE_CSS_SOURCE)
    .pipe(gulp.dest(SITE_CSS_DEST));
});

// TASK: Copy all of the fullpage javascripts to the deployment directory
gulp.task('javascript-fullpage', function() {
  return gulp.src(FULLPAGE_JAVASCRIPT_SOURCE)
    .pipe(gulp.dest(FULLPAGE_JAVASCRIPT_DEST));
});

// TASK: Copy all of the fullpage javascripts to the deployment directory
gulp.task('css-fullpage', function() {
  return gulp.src(FULLPAGE_CSS_SOURCE)
    .pipe(gulp.dest(FULLPAGE_CSS_DEST));
});

// TASK: automatically perform the full deploy when files change
gulp.task('deploy-watch', function() {
  gulp.watch(['*.html', 'css/*.css', 'js/*.js'], gulp.series('deploy'))
});

// TASK: perform the full deploy
gulp.task(
  'deploy',
  gulp.parallel('html-site', 'css-site', 'javascript-fullpage', 'css-fullpage')
);

// }}}

// Default {{{

gulp.task('default', gulp.series('deploy'));

// }}}
