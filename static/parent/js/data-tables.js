(function($) {
  'use strict';
var dataSet = [
    [ "Tiger Nixon", "System Architect", "10th", "50,000", "25,000", "25,000" ],
,

    
  ];



var dataSet2 = [
  // [ "Tiger Nixon", "System Architect", "10th", "50,000", "25,000", "25,000" ],

    
  ];

var dataSet3 = [
  
    [ "Tiger Nixon", "System Architect", "B.Tech", "5421789", "2011/04/25", "$320,800" ],

    
  ];
      // fee details
    var dataSet4 = [
    // [ "Tiger Nixon", "1", "B.Tech", "5421789", "2011/04/25", "$135" ],
     [ "Jan", "101", "10th", "2022/10/10", "25,000", "25,000","due date" ],


    
  ];
    
  var dataSet5 = [
    [ "Meachnical Engg", "Kalvine", "7829828", "kr@gmail.com", "1998", "135" ],

  ];
    

    
    
    
     var dataSet6 = [
    [ "A", "1", "Medium", "2", "2", "20$" ],
     [ "B", "2", "small", "6", "4", "10$" ],
    [ "C", "3", "Large", "12", "10", "15$" ],
    [ "D", "23", "Medium", "3", "2", "5$" ],
     [ "E", "45", "Large", "4", "3", "20$" ],
    [ "F", "36", "small", "2", "2", "10$" ],
    [ "A", "1", "Medium", "2", "2", "20$" ],
     [ "B", "2", "small", "6", "4", "10$" ],
    [ "C", "3", "Large", "12", "10", "15$" ],
    [ "D", "23", "Medium", "3", "2", "5$" ],
     [ "E", "45", "Large", "4", "3", "20$" ],
    [ "F", "36", "small", "2", "2", "10$" ],
    [ "A", "1", "Medium", "2", "2", "20$" ],
     [ "B", "2", "small", "6", "4", "10$" ],
    [ "C", "3", "Large", "12", "10", "15$" ],
    [ "D", "23", "Medium", "3", "2", "5$" ],
     [ "E", "45", "Large", "4", "3", "20$" ],
    [ "F", "36", "small", "2", "2", "10$" ],
    [ "A", "1", "Medium", "2", "2", "20$" ],
     [ "B", "2", "small", "6", "4", "10$" ],
    [ "C", "3", "Large", "12", "10", "15$" ],
    [ "D", "23", "Medium", "3", "2", "5$" ],
     [ "E", "45", "Large", "4", "3", "20$" ],
    [ "F", "36", "small", "2", "2", "10$" ],
    
  ];
    
    
 var dataSet7 = [
    [ "john", "1234567", "VX-235", "VX-234", "Brokylen to botanic", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "john Lary", "2234567", "DX-235", "CX-234", "Brokylen to Newyork", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "Korey", "13456745", "KX-435", "TX-234", "Brokylen to Washingaton", "<i class='fas fa-map-marked-alt'></i>" ],
    [ "john", "1234567", "VX-235", "VX-234", "Brokylen to botanic", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "john Lary", "2234567", "DX-235", "CX-234", "Brokylen to Newyork", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "Korey", "13456745", "KX-435", "TX-234", "Brokylen to Washingaton", "<i class='fas fa-map-marked-alt'></i>" ],
    [ "john", "1234567", "VX-235", "VX-234", "Brokylen to botanic", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "john Lary", "2234567", "DX-235", "CX-234", "Brokylen to Newyork", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "Korey", "13456745", "KX-435", "TX-234", "Brokylen to Washingaton", "<i class='fas fa-map-marked-alt'></i>" ],
    [ "john", "1234567", "VX-235", "VX-234", "Brokylen to botanic", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "john Lary", "2234567", "DX-235", "CX-234", "Brokylen to Newyork", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "Korey", "13456745", "KX-435", "TX-234", "Brokylen to Washingaton", "<i class='fas fa-map-marked-alt'></i>" ],
    [ "john", "1234567", "VX-235", "VX-234", "Brokylen to botanic", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "john Lary", "2234567", "DX-235", "CX-234", "Brokylen to Newyork", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "Korey", "13456745", "KX-435", "TX-234", "Brokylen to Washingaton", "<i class='fas fa-map-marked-alt'></i>" ],
    [ "john", "1234567", "VX-235", "VX-234", "Brokylen to botanic", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "john Lary", "2234567", "DX-235", "CX-234", "Brokylen to Newyork", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "Korey", "13456745", "KX-435", "TX-234", "Brokylen to Washingaton", "<i class='fas fa-map-marked-alt'></i>" ],
    [ "john", "1234567", "VX-235", "VX-234", "Brokylen to botanic", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "john Lary", "2234567", "DX-235", "CX-234", "Brokylen to Newyork", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "Korey", "13456745", "KX-435", "TX-234", "Brokylen to Washingaton", "<i class='fas fa-map-marked-alt'></i>" ],
    [ "john", "1234567", "VX-235", "VX-234", "Brokylen to botanic", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "john Lary", "2234567", "DX-235", "CX-234", "Brokylen to Newyork", "<i class='fas fa-map-marked-alt'></i>" ],
     [ "Korey", "13456745", "KX-435", "TX-234", "Brokylen to Washingaton", "<i class='fas fa-map-marked-alt'></i>" ],
     
  ];
    
   
     var dataSet8 = [
    [ "Lorvil", "20", "Cricket", "Male", "State", "2" ],
     [ "Kery", "23", "Volyball", "Female", "District", "1" ],
     [ "John", "25", "basketball", "Male", "National", "4" ],
     [ "Lucy", "20", "Rifle Shooting", "Female", "international", "4" ],
     [ "Elvine", "24", "Gymanstic", "Male", "National", "6" ],
    [ "Lorvil", "20", "Cricket", "Male", "State", "2" ],
     [ "Kery", "23", "Volyball", "Female", "District", "1" ],
     [ "John", "25", "basketball", "Male", "National", "4" ],
     [ "Lucy", "20", "Rifle Shooting", "Female", "international", "4" ],
     [ "Elvine", "24", "Gymanstic", "Male", "National", "6" ],
 [ "Lorvil", "20", "Cricket", "Male", "State", "2" ],
     [ "Kery", "23", "Volyball", "Female", "District", "1" ],
     [ "John", "25", "basketball", "Male", "National", "4" ],
     [ "Lucy", "20", "Rifle Shooting", "Female", "international", "4" ],
     [ "Elvine", "24", "Gymanstic", "Male", "National", "6" ],
    
  ];     
    
 var dataSet9 = [
    [ "1", "New Year's Day", "Public Holiday", "01 January 2021", "03 January 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "2", "Memorial Day", "Public Holiday", "29 May 2021", "29 May 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "3", "Christmas Day", "Public Holiday", "25 December 2021", "03 January 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "4", "Holiday By Collage", "Public Holiday", "03 March 2021", "09-March 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "5", "New Year's Day", "Public Holiday", "01 January 2021", "03 January 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "6", "Memorial Day", "Public Holiday", "29 May 2021", "29 May 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "7", "Christmas Day", "Public Holiday", "25 December 2021", "03 January 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "8", "Holiday By Collage", "Public Holiday", "03 March 2021", "09-March 2021", "Lorem Ipsum is simply dummy text of the printing" ],
    [ "9", "New Year's Day", "Public Holiday", "01 January 2021", "03 January 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "10", "Memorial Day", "Public Holiday", "29 May 2021", "29 May 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "11", "Christmas Day", "Public Holiday", "25 December 2021", "03 January 2021", "Lorem Ipsum is simply dummy text of the printing" ],
     [ "12", "Holiday By Collage", "Public Holiday", "03 March 2021", "09-March 2021", "Lorem Ipsum is simply dummy text of the printing" ],
  ];     
        
    
    
  var tableOne = $('#data-table-1').DataTable( {
    data: dataSet,
    columns: [
      { title: "Name" },
      { title: "Departement" },
      { title: "Degree" },
      { title: "Mobile" },
      { title: "Joining date" },
      { title: "Salary" }
    ],
  });
  var tableTwo = $('#data-table-2').DataTable( {
    data: dataSet4,
    columns: [
      { title: "Month" },
      { title: "Roll No" },
      { title: "Class" },
      { title: "Due Date" },
      { title: "Tottal Payed" },
      { title: "Pending Fee" }
    ],
  });
  var tableThree = $('#data-table-3').DataTable( {
    data: dataSet3,
    columns: [
      { title: "Name" },
      { title: "Desgination" },
      { title: "Degree" },
      { title: "Mobile" },
      { title: "Joining date" },
      { title: "Salary" }
    ],
    scrollY: 400
  });
  var tableFour = $('#data-table-4').DataTable( {
    data: dataSet2,
    columns: [
      { title: "Name" },
      { title: "Roll No" },
      { title: "Class" },
        { title: "Due Date" },
      { title: "Tottal Payed" },
      { title: "Pending Fee" }
    
      
    ],
  });
    
   var tableOne = $('#data-table-5').DataTable( {
    data: dataSet5,
    columns: [
      { title: "Departement Name" },
      { title: "Head of Dept" },
      { title: "Phone" },
      { title: "Email" },
      { title: "Starting Year" },
      { title: "Student Capacity" }
    ],
  });  
    
    var tableOne = $('#data-table-6').DataTable( {
    data: dataSet6,
    columns: [
      { title: "Block" },
      { title: "Room No" },
      { title: "Type" },
      { title: "Number Of Bed" },
      { title: "Avalibality" },
      { title: "Cost Per Bed" }
    ],
  });  
    
     var tableOne = $('#data-table-7').DataTable( {
    data: dataSet7,
    columns: [
      { title: "Driver Name" },
      { title: "Mobile Number" },
      { title: "Licence Number" },
      { title: "Vehicle Number" },
      { title: "Route Name" },
      { title: "MAP" }
    ],
  });
     var tableOne = $('#data-table-8').DataTable( {
    data: dataSet8,
    columns: [
      { title: "Name" },
      { title: "Age" },
      { title: "Sport Name" },
      { title: "Gender" },
      { title: "Sport Level" },
      { title: "Wins Medal" }
    ],
  });    
    
    var tableOne = $('#data-table-9').DataTable( {
    data: dataSet9,
    columns: [
      { title: "#" },
      { title: "Title" },
      { title: "Type" },
      { title: "Start-Date" },
      { title: "End-date" },
      { title: "Details" }
    ],
  });    
    
    
})(jQuery);
