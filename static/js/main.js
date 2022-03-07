$(document).ready(function(){
    $('#country').change(function(){
        $.ajax({
            url: $("#person-form").attr("get-states"),
            type: 'get',
            data: {
                country: $(this).val()
            },
            success: function(response){
                html_data = "<option value=''>------</option>" 
                response.forEach(function(state){
                    html_data += `<option value="${state.name}">${state.name}</option>`;
                })
                $("#state").html(html_data);
            }
        });
    });
    $('#state').change(function(){
        $.ajax({
            url: $("#person-form").attr("get-districts"),
            type: 'get',
            data: {
                state: $(this).val()
            },
            success: function(response){
                html_data = "<option value=''>------</option>"
                response.forEach(function(district){
                    html_data += `<option value="${district.name}">${district.name}</option>`;
                })
                $("#district").html(html_data);
            }
        });
    });
    $('#district').change(function(){
        $.ajax({
            url: $("#person-form").attr("get-cities"),
            type: 'get',
            data: {
                district: $(this).val()
            },
            success: function(response){
                html_data = "<option value=''>------</option>"
                response.forEach(function(city){
                    html_data += `<option value="${city.name}">${city.name}</option>`;
                })
                $("#city").html(html_data);
            }
        });
    });
});