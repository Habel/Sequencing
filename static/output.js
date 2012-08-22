$(document).ready(function() {
    // make sure all readonly things (denoted by readonly class) are actually readonly
    $(".readonly").keydown(function(keydown_event) {
        // allow arrow keys to move around and f5 to refresh
        // left: 37
        // up: 38
        // right: 39
        // down: 40
        // f5: 116
        code = keydown_event.keyCode
        return ((code >= 37 && code <= 40) || code == 116)
    });    

    // make sure all the tracked textareas pos_tracker's get updated on entry
    $(".tracked").on("keyup click", function() {
        dist_from_start = this.selectionStart;
        $("#pos_" + this.id).text(dist_from_start);
    });

    // set the text of something
    var set_text_of_id = function(id, message)
    {
        $("#" + id).text(message);
    };

    // this is for when the user done goofed
    var set_error_message = function(message) 
    {
        set_text_of_id("error_message", message);
    };

    // count the occurrences of a value in a sequence
    var count = function(sequence, toFind)
    {
        sequence = sequence.toLowerCase();
        var occurred = 0;

        $.each(sequence, function(index, val) {
            if(val === toFind)
                occurred++;
        });

        return occurred;
    };

    // make sure the dna string only has a,c,t,g
    var is_valid = function(sequence)
    {
        // check to make sure there are no characters that aren't a, c, t, or g
        sequence = sequence.toLowerCase();
        return $.grep(sequence, function(elem, index) { return "actg".indexOf(elem) == -1 }).length == 0;
    }

    $("#submit_button").click(function() {
        
        // reset the error message from last click
        set_error_message("");

        var seq1 = $("#seq1").val();
        var seq2 = $("#seq2").val();

        var seq1_len = seq1.length
        var seq2_len = seq2.length

        // check to make sure that both sequences are valid
        if(seq1_len < 100)
            set_error_message("Sequence 1 is too short")
        else if(seq1_len > 20000)
            set_error_message("Sequence 1 is too long")
        else if(!is_valid(seq1))
            set_error_message("Sequence 1 does not consist of only a, c, t, and g");

        else if(seq2_len < 15)
            set_error_message("Sequence 2 is too short");
        else if(seq2_len > 17000)
            set_error_message("Sequence 2 is too long");
        else if(!is_valid(seq2))
            set_error_message("Sequence 2 does not consist of only a, c, t, and g");

        // set the outputs
        set_text_of_id("seq1_len", seq1_len);
        set_text_of_id("seq2_len", seq2_len);

        // if the user is privilege 1, cg_occurrence will be in the page
        if($("#cg_occurrence").length > 0)
            set_text_of_id("cg_occurrence", count(seq1, 'c') + count(seq1, 'g'));
        
        // special case for output sequence because textareas can't use .text()
        $("#output_textarea").val(seq1);
    });
});
