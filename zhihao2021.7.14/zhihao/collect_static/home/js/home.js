function turn_zhongyang(){
	little=document.getElementsByClassName('little')[0]
	
	if (window.getComputedStyle(little,null).display ==='block'){
		little.style.display='none';
	}
	else{
		little.style.display='block';
	}
}