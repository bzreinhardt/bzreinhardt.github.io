var active_section;
function record_jump(active_section_id){
	document.querySelector(`li a[href="#${active_section_id}"]`).parentElement.classList.remove('active');
	tracker = document.getElementById("tracker");
	tracker.firstElementChild.href = "#"+active_section_id;
	var active_section_name = document.getElementById(active_section_id).innerText;
	tracker.firstElementChild.innerText = "Jump back to: "+ active_section_name;
}
//TODO - fix that queryselector grabs the tracker
$('.internal-link').click(function(){
	record_jump(active_section);
});


window.addEventListener('DOMContentLoaded', () => {


	const observer = new IntersectionObserver(entries => {
		var max_ratio = 0;
		var max_ratio_id = null;
		entries.forEach(entry => {
			if (entry.intersectionRatio > 0) {
				if (entry.intersectionRatio > max_ratio) {
					max_ratio = entry.intersectionRatio;
					max_ratio_id = entry.target.getAttribute('id');
				}
			}
		});
		if (active_section != max_ratio_id) {
			if (active_section && max_ratio_id) {
				var sections = document.querySelector(`li:not(#tracker) a[href="#${active_section}"]`).parentElement.classList.remove('active');
			}
			if (max_ratio_id) {
				active_section = max_ratio_id;
				document.getElementById('current_section_label').innerText = document.getElementById(active_section).innerText;
				document.querySelector(`li:not(#tracker) a[href="#${active_section}"]`).parentElement.classList.add('active');
			}
		}

	});

	// Track all sections that have an `id` applied
	document.querySelectorAll('h1[id]').forEach((section) => {
		observer.observe(section);
	});
	document.querySelectorAll('h2[id]').forEach((section) => {
		observer.observe(section);
	});
	document.querySelectorAll('h3[id]').forEach((section) => {
		observer.observe(section);
	});

});
