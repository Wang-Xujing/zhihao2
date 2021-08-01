function openTab(data, index, selected, loading) {
	if (data.breadcrumbs) {
		this.breadcrumbs = data.breadcrumbs;
	}
	//如果data没有eid，就直接打开或者添加，根据url
	if (!data.eid) {
		data.eid = new Date().getTime() + "" + Math.random();
	}

	if (index) {
		this.menuActive = String(index);
	}
	if (selected) {
		//找到name，打开
		// console.log(data)
		for (var i = 0; i < this.tabs.length; i++) {
			if (this.tabs[i].url == data.url) {
				this.tabModel = this.tabs[i].id;
				break;
			}
		}
		return;
	}

	this.breadcrumbs = data.breadcrumbs;
	var exists = null;
	//判断是否存在，存在就直接打开
	

	if (exists) {
		this.tabModel = exists.id;
	} else {
		//其他的网址loading会一直转
		if (data.url && data.url.indexOf('http') != 0) {
			if (loading) {
				data.loading = true;
				this.loading = true;
			} else {
				data.loading = false;
				this.loading = false;
			}
		}
		// data.id = new Date().getTime() + "" + Math.random();
		data.id = data.eid;
		data.index = index;
		// this.tabs.push(data);
		this.tabModel = data.id;
	}
	// changeUrl(data)
	// this.syncTabs();
}
