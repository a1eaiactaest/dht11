function Paragraph(props) {
  return <p className={`${props.styleName}`}>{props.children}</p>;
}

export { Paragraph };
