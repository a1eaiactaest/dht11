function Navbar(props) {
  /*
    Takes props.elements as main prop.

    It should look like:
    [
      ['Home', '/dashboard'],
      ['Team', '/team'],
      ['Projects', '/projects'],
      ['Reports', '/reports'],
    ]
  */

  var NavBarElements = props.elements.map(([title, url]) => (
    <a key={url} href={url} className="rounded-lg px-3 py-2 text-slate-900 font-medium hover:bg-slate-900 hover:text-green-400">{title}</a>
  ));

  return (
    <nav className="flex sm:justify-center space-x-4">
      <ul>{NavBarElements}</ul>
    </nav>
  );
}

export default Navbar;