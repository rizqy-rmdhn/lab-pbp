$(document).ready(function () {
    $("form").submit(function (event) {
      var formData = {
        name: $("#nama_barang").val(),
        email: $("#harga_barang").val(),
        superheroAlias: $("#deskripsi_barang").val(),
      };
  
      $.ajax({
        type: "POST",
        url: "{% url 'wishlist_ajax' %}",
        data: formData,
        dataType: "json",
        encode: true,
      }).done(function (data) {
        console.log(data);
      });
  
      event.preventDefault();
    });
  });