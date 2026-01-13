
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    contrastThreshold: 4.5,
  },
  colorSchemes: {
    light: true,
    dark: true,
  },
})

export default theme;

/*
  function App() {
  return <ThemeProvider theme={theme}>...</ThemeProvider>;
  }
*/
