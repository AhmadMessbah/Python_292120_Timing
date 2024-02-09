
    let idCounter = 1;

    function addRow() {
      const dataTable = document.getElementById("dataTable");
      const formData = new FormData(document.getElementById("dataForm"));
      const newRow = dataTable.insertRow(-1);
      newRow.insertCell().textContent = idCounter++;

      for (const value of formData.values()) {
        const cell = newRow.insertCell();
        cell.textContent = value;
      }
    }
