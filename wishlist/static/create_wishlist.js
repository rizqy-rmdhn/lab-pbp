$(document).ready(function () {
    $("form").submit(function (event) {
      var formData = {
        nama_barang: $("#nama_barang").val(),
        harga_barang: $("#harga_barang").val(),
        deskripsi_barang: $("#deskripsi_barang").val(),
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