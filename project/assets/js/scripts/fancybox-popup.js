$(document).ready(function($) {

  // easy photo and video gallery
  $('.js-gallery-fancybox').fancybox({
    nextEffect: 'fade',
    prevEffect: 'fade',
    wrapCSS: 'fancybox-gallery-skin', // styles are in file css/components/popup.styl
    helpers: {
      media: true, // for video gallery
      title : {
        type : 'inside'
      }
    }
  });


  function getTitle(obj){
    var str = '<div class="fancybox-title-wrap">'
    str += '<div class="fancybox-title-wrap__main">'+ (obj.title ? '' + obj.title + '' : '') +'</div>';
    
    str += '<div class="fancybox-title-wrap__counter">';

    str += '<a href="javascript:parent.$.fancybox.prev();" class="fancybox-title-wrap__prev">пред</a>';
    str += '<div>' + (obj.index + 1) + '/' + obj.group.length + '</div>';
    str += '<a href="javascript:parent.$.fancybox.prev();" class="fancybox-title-wrap__prev">дальше</a>';
    

    str += '</div></div>'

    return str;
  }

  // popup
  $('.js-popup-fancybox').fancybox({
    nextEffect: 'fade',
    prevEffect: 'fade',

    helpers : {
      title : {
        type : 'inside'
      }
    },
    beforeShow : function() {
      var title = getTitle(this);

      this.title = title;
      // (this.title ? '' + this.title + '' : '') + 'Image ' + (this.index + 1) + ' of ' + this.group.length;
    }
  });

});