function commentFormatDate(dateString) {
  const date = new Date(dateString);
  const options = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  };
  const formattedDate = new Intl.DateTimeFormat('en-US', options).format(date);

  return formattedDate;
}

export default commentFormatDate;
