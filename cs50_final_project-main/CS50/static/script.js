
var tabbedNav = (function() {
  
  var $this = '';
  var $href = '';
  var $menuID = '';
  var $currentMenu = '';
     
  var $navSecondary = '.nav--secondary';
  
  $('.nav--primary > li > a').click(function( event ){

    event.preventDefault();
    
    /***********************************
    1. collect href
    2. strip out foreward slashes
    3. assign as current menu
    ************************************/
    //$this = $(this).find('> a');
    $href = $(this).attr('href');
    $menuID = $href.slice(1, -1);
    $currentMenu = "[data-menu='" + $menuID + "']";
    
    
    // Check if clicked link has a subnav
    if ( $(this).hasClass('has-submenu') === true ) {
      
      // Do nothing if current menu is already open
      if ($('ul').find($currentMenu).hasClass('active') === false) {

        // Move current menu to top of stack
        $($navSecondary).find($currentMenu).appendTo($navSecondary);

        /* appending and animating CSS simultaneously 
        breaks the transition. adding a miillisecond 
        timeout before adding active class fixes this */
        
        setTimeout(function() {   

          // activate new menu items
          $('.nav--primary > li > a[href="' + $href + '"]').parent().addClass('active');         
          $($navSecondary).find($currentMenu).addClass('active');

          // deactivate old menu link
          $(".nav--primary li a:not([href='" + $href + "'])").parent().removeClass('active');

          // wait until transition ends
          setTimeout(function() {

            // deactivate old menu
            $('.menu').not($currentMenu).removeClass('active');
            
          }, 200); // timer should match CSS transition

        }, 10);
      }
    }  
  });
	
  // Trigger Dropdown
  function openDropdown(event){
    
    $(this).siblings('ul').slideDown(250);
    if ($(this).parent().hasClass('has-dropdown')) {
      $(this).addClass('active');
      event.stopPropagation();
    }
  }
  
  $('.nav--secondary > ul > li > a').unbind().click( openDropdown );
  
  
  // Close Dropdown
  function closeDropdown() {  
    $('.nav--secondary > ul > li').find('ul').slideUp(250);
    $('.nav--secondary > ul > li').find('.active').removeClass('active');
  }
  
  $(document).click(function(e){
  
    if (! $(e.target).parents().hasClass('has-dropdown')) {
      closeDropdown()
    }
  });

})();