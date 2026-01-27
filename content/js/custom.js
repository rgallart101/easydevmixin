<script>
    $(document.links).filter(function() {
        return this.hostname != window.location.hostname;
    })
        .attr('target', '_blank')
        .attr('rel', 'nofollow');
</script>
