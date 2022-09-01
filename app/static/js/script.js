document.addEventListener("DOMContentLoaded", function () {
    const options = {
        "edge": "left"
    }

    var elems = document.querySelectorAll(".sidenav");
    var instances = M.Sidenav.init(elems, options);
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    var instances = M.FloatingActionButton.init(elems);
  });

  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);
  });
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
  });

  function course_query(){

    var enquiry_id =document.getElementById('enquiry_id').value
    var category =document.getElementById('category').value
    var course =document.getElementById('course').value
    var status = document.getElementById('status').value
    var instructor =document.getElementById('instructor').value

    window.location.href="/admin/enquiry" + URLSearchParams({
      "course_id": course_id
    })
  }

  function addcourse() {
    window.location.href = '/admin/courses'
  }

  function deletecourse(courseId) {
    fetch('/admin/courses/'+courseId, {
        method: 'DELETE'
    }).then(() => window.location.href = '/admin/courses')
  }
