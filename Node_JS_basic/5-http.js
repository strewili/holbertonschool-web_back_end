const http = require('http');
const fs = require('fs');

const database = process.argv[2];

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const output = [`Number of students: ${students.length}`];
      const fields = {};

      students.forEach((line) => {
        const parts = line.split(',');
        const firstName = parts[0];
        const field = parts[parts.length - 1];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstName);
      });

      Object.keys(fields).forEach((field) => {
        const list = fields[field];

        output.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });

      resolve(output.join('\n'));
    });
  });
}

const app = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' });

  if (request.url === '/') {
    response.end('Hello Holberton School!');
  } else if (request.url === '/students') {
    countStudents(database)
      .then((report) => {
        response.end(`This is the list of our students\n${report}`);
      })
      .catch((error) => {
        response.end(`This is the list of our students\n${error.message}`);
      });
  } else {
    response.end();
  }
});

app.listen(1245).on('error', () => {});

module.exports = app;
