#!/usr/bin/node

const fs = require('fs')

const filePath = process.argv[2]
const string_data = process.argv[3]

fs.writeFile(filePath, string_data, (err) => {

	if (err){
		console.error(err)
		return
	}
});
