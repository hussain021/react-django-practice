import React, { useEffect, useState } from "react";
import AppButton from "./AppButton";

export default function Pagination({ data, dataLimit, onClick }) {
  const [pages, setPages] = useState(Math.round(data.length / dataLimit));
  const [currentPage, setCurrentPage] = useState(1);

  useEffect(() => {
    setPages(Math.ceil(data.length / dataLimit));
  });

  function goToNextPage() {
    setCurrentPage((page) => page + 1);
    onClick(currentPage);
  }

  function goToPreviousPage() {
    setCurrentPage((page) => page - 1);
    onClick(currentPage);
  }

  return (
    <React.Fragment>
      <div className="pagination">
        <AppButton
          onClick={goToPreviousPage}
          className={`prev ${currentPage === 1 ? "disabled" : ""}`}
          text="prev"
        />

        <AppButton
          onClick={goToNextPage}
          className={`next ${currentPage === pages ? "disabled" : ""}`}
          text="next"
        />
      </div>
    </React.Fragment>
  );
}

//source for this code: https://academind.com/tutorials/reactjs-pagination . The code was first completly understood and then copied and changed to my needs
