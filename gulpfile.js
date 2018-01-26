var pathAssets = './catalog/static'
'use strict';
 
var gulp = require('gulp');
var sass = require('gulp-sass');
 
gulp.task('sass', function () {
  return gulp.src('./build/sass/**/*.scss')
    .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
    .pipe(gulp.dest(pathAssets + '/css'));
});

gulp.task('watch', function () {
  gulp.watch('./build/sass/**/*.scss', ['sass']);
});

gulp.task('styles', function(){
    console.log('running styles');
})