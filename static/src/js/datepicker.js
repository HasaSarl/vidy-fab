odoo.define('vidy-fab.datepicker', function(require) {
    "use strict";
    var Widget = require('web.datepicker');

    Widget.DateWidget.include({
        set_datetime_default: function() {
            //when opening datetimepicker the date and time by default should be the one from
            //the input field if any or the current day otherwise
            var value = moment().second(0);
            if(this.$input.val().length !== 0 && this.is_valid()) {
                value = this.$input.val();
            }
            var d = moment(this.$input.val(), "DD. MM. YYYY")
            if(this.el.classList.contains("nodatepicker") && moment().isSame(d, "day")) {
                this.picker.setValue("")
                return
             }
                 // temporarily set pickTime to true to bypass datetimepicker hiding on setValue
            // see https://github.com/Eonasdan/bootstrap-datetimepicker/issues/603
            var saved_picktime = this.picker.options.pickTime;
            this.picker.options.pickTime = true;
            this.picker.setValue(value);
            this.picker.options.pickTime = saved_picktime;
        },    
    });
});
