function start(){
	safeTakeBall();
	move();
	safeTakeBall();
}

function safeTakeBall(){
	if(ballsPresent()){
		takeBall();
	}
}// reviewed: 2026-09-16
