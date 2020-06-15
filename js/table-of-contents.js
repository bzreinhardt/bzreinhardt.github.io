window.addEventListener('DOMContentLoaded', () => {

	var active_section;
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
				document.querySelector(`li a[href="#${active_section}"]`).parentElement.classList.remove('active');
			}
			if (max_ratio_id) {
				active_section = max_ratio_id;
				document.getElementById('current_section_label').innerText = document.getElementById(active_section).innerText;
				document.querySelector(`li a[href="#${active_section}"]`).parentElement.classList.add('active');
			}
		}
		/*

				//if active_section still in
				document.querySelector(`li a[href="#${active_section}"]`).parentElement.classList.remove('active');
				active_section = id;
				document.querySelector(`li a[href="#${id}"]`).parentElement.classList.add('active');
			} else {
				document.querySelector(`li a[href="#${id}"]`).parentElement.classList.remove('active');
			}
			*/

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
