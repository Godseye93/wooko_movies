function formatDate(dateString) {
  const date = new Date(dateString);
  const options = {
    year: 'numeric',
    month: 'numeric',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  };
  const formattedDate = new Intl.DateTimeFormat('en-US', options).format(date);

  // 날짜와 시간을 구분하기 위해 공백을 추가
  const [datePart, timePart] = formattedDate.split(' ');

  // 날짜 부분을 '/'로 구분하여 순서를 변경
  const [day, month, year] = datePart.split('/');
  const reorderedDate = `${year.replace(/,/, '')}/${month}/${day}`;

  return `${reorderedDate} ${timePart}`;
}

export default formatDate;
