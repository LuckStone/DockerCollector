overview = function () {
	var data = {};
    data['namespace'] = db.Namespace.find().count();
	data['user'] = db.User.find().count();
	data['repository'] = db.Repository.find().count();
	data['comment'] = db.Comment.find().count();
	data['tag'] = db.Tag.find().count();

	return {"result":0, "content":data};
}