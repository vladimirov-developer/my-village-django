var gulp = require('gulp'),
    watch = require('gulp-watch'),
    plumber = require('gulp-plumber'),

    // jade
    pug = require('gulp-pug'),
    pugInheritance  = require('gulp-pug-inheritance'),
    changed = require('gulp-changed'),
    cached = require('gulp-cached'),
    filter = require('gulp-filter'),
 
    // stylus
    stylus = require('gulp-stylus'),
    csso = require('gulp-csso'),
    prefix = require('gulp-autoprefixer'),

    // svg
    svgstore = require('gulp-svgstore'),
    svgmin = require('gulp-svgmin'),
    base64 = require('gulp-base64-inline'),

    gutil = require('gulp-util'),
    gulpif = require('gulp-if'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    webserver = require('gulp-webserver'),
    coffee = require('gulp-coffee'),
    requi = require('gulp-requi');

// Set some defaults
var isDev = true;
var isProd = false;

// If "production" is passed from the command line then update the defaults
if (gutil.env.type === 'production') {
    isDev = false;
    isProd = true;
}

gulp.task('svgstore', function() {
    return gulp
        .src('project/assets/img/svgstore/*.svg')
        .pipe(gulpif(isProd, svgmin()))
        .pipe(svgstore())
        .pipe(gulp.dest('./project/templates/'));
});

gulp.task('svg', function() {
    return gulp
        .src(['./project/assets/img/svg/*.svg'])
        .pipe(svgmin())
        .pipe(gulp.dest('./project/assets/img/base64'));
});

gulp.task('svg_plan', function() {
    return gulp
        .src(['./project/assets/img/plan/*.svg'])
        // .pipe(svgmin())
        .pipe(svgmin({
            plugins: [{
                cleanupIDs: {
                    remove: false,
                    minify: true
                }, 
                addAttributesToSVGElement: {
                    attribute: 'data-icon'
                }
            }]
        }))
        .pipe(gulp.dest('./project/templates/plan'));
});

gulp.task('stylus', function() {
    gulp.src(['./project/assets/stylus/style.styl'])
        .pipe(plumber())
        .pipe(stylus())
        .pipe(prefix())
        .pipe(base64('../../assets/img/base64'))
        .pipe(gulpif(isProd, csso()))
        .pipe(gulp.dest('./project/static/css/'));
});

gulp.task('js', function() {
    gulp.src(['./project/assets/js/scripts.js'])
        .pipe(requi())
        .pipe(gulpif(/[.]coffee$/, coffee())).on('error', console.log)
        .pipe(gulpif(isProd, uglify({
            compress: {
                drop_console: true
            }
        })))
        .pipe(concat('scripts.js'))
        .pipe(gulp.dest('./project/static/js'));
});


gulp.task('watch', function() {
    watch('./project/assets/stylus/**/**/*.styl', function(event) {
        gulp.start('stylus');
    });
    watch('./project/assets/js/**/**/*.js', function(event) {
        gulp.start('js');
    });

    gulp.watch('project/assets/img/svgstore/*.svg', ['svgstore']);
    gulp.watch('project/assets/img/svg/*.svg', ['svg']);
    gulp.watch('project/assets/img/plan/*.svg', ['svg_plan']);
});

gulp.task('build', ['js', 'svg', 'svg_plan', 'stylus']);
gulp.task('default', ['build', 'watch']);