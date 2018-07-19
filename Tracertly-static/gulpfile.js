const gulp = require('gulp');
const sass = require('gulp-sass');
const browserSync = require('browser-sync').create();
const useref = require('gulp-useref');
const uglify = require('gulp-uglify');
const gulpIf = require('gulp-if');
const nano = require('cssnano');
const cssnano = require('gulp-cssnano');
const imagemin = require('gulp-imagemin');
const cache = require('gulp-cache');
const del = require('del');
const runSequence = require('run-sequence');
const autoprefixer = require('autoprefixer');
const sourcemaps = require('gulp-sourcemaps');
const babel = require('gulp-babel');
const postcss = require('gulp-postcss');

//Task for sass
gulp.task('sass', function(){
  return gulp.src('app/scss/**/*.scss')
    .pipe(sass()) // Converts Sass to CSS with gulp-sass
    .pipe(postcss([autoprefixer({browsers: ['last 2 versions']}), nano()]))  // to usewith cssnano
    .pipe(gulp.dest('app/css'))
    .pipe(browserSync.reload({
      stream: true
    }))
});

// Browser Sync
gulp.task('browserSync', function() {
  browserSync.init({
    server: {baseDir: 'app'}
  })
})

// Optimizing CSS and JavaScript files
	// concatenate js script tags into dist/js/main.min.js
gulp.task('useref', function(){
  return gulp.src('app/*.html')
    .pipe(useref())
    .pipe( // Writing ES6 with Babel
    	gulpIf('*.js',
    		babel({
            	presets: ['env']
        })))
    // Minifies only if it's a JavaScript file
    .pipe(gulpIf('*.js', uglify()))    
    // Minifies only if it's a CSS file
    .pipe(gulpIf('*.css', cssnano()))
    .pipe(gulp.dest('dist'))
});

// Optimizing Images
// Optimizing images however, is an extremely slow process 
// that you'd not want to repeat unless necessary
gulp.task('images', function(){
  return gulp.src('app/images/**/*.+(png|jpg|gif|svg)')
  // Caching images that ran through imagemin
  .pipe(cache(imagemin({
  	  // create interlaced GIFs by setting the 
  	  // interlaced option key to true if you want
      interlaced: true
    })))
  .pipe(gulp.dest('dist/images'))
});

// Writing ES6 with Babel
gulp.task('babell', () =>
    gulp.src('app/js/**/*.js')
        .pipe(sourcemaps.init())
        .pipe(babel({
            presets: ['env']
        }))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('dist/js'))
);

// Autoprefixer
// Using Autoprefixer to write vendor-free CSS code
gulp.task('autoprefixer', function () {
    return gulp.src('app/**/*.css')
    	// Adding Sourcemaps for easier debugging
        .pipe(sourcemaps.init())
        .pipe(postcss([ autoprefixer() ]))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('app/css'));
});

// Copying Fonts to Dist
gulp.task('fonts', function() {
  return gulp.src('app/fonts/**/*')
  .pipe(gulp.dest('dist/fonts'))
})

// Cleaning up generated files automatically
gulp.task('clean', function() {
  return del.sync('dist');
})

gulp.task('clean:css', function() {
  return del.sync('app/css');
})


gulp.task('clean:dist', function() {
  return del.sync(['dist/**/*', '!dist/images', '!dist/images/**/*']);
});

// Clear cached images
gulp.task('cache:clear', function (callback) {
	return cache.clearAll(callback)
})

// watch for changes
gulp.task('watch', ['browserSync', 'sass', 'autoprefixer'], function(){
  gulp.watch('app/scss/**/*.scss', ['sass']);
  // gulp.watch('app/css/**/*.css', postcss([ autoprefixer() ]));
  // Reloads the browser whenever HTML or JS files change
  gulp.watch('app/*.html', browserSync.reload);
  gulp.watch(
    'app/js/**/*.js', [
      babel({presets: ['env']}) , 
      browserSync.reload
  ]);
})

gulp.task('build', function (callback) {
  runSequence(
  	['clean:dist', 'clean:css'],
    'sass',
    'useref', 
    'images', 
    'fonts'
  )
})

gulp.task('default', function (callback) {
  runSequence(['sass', 'browserSync'], 'watch',
    callback
  )
})

// get bootstrap js and j query js
gulp.task('get-bj', function() { 
        return gulp.src
            ([
            'node_modules/jquery/dist/jquery.js', 
            'node_modules/bootstrap/dist/js/bootstrap.js', 
            ])
        .pipe(gulp.dest('app/js/'));
});


// echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p