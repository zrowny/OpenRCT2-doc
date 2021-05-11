function openTarget() {
    console.log("opening target...")
    var $target = $(location.hash);
    if ($target.is(":hidden")) {
        if ($target.is("details")) {
            $target.prop("open", true);
        }
        else {
            $target.next().prop("open", true);
        }
        $target.parents("details").prop("open", true);
    }
    $target.get(0).scrollIntoView();
}

$(window).on('hashchange', function() {
    openTarget()
});
//$('body').on('click', "[href^='#']", function(){openTarget()});
openTarget();