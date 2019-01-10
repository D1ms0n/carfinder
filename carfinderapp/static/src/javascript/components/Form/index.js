import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import 'rc-slider/assets/index.css';
import 'react-select/dist/react-select.css';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import Input from '@material-ui/core/Input';
import MenuItem from '@material-ui/core/MenuItem';
import ArrowDropDownIcon from '@material-ui/icons/ArrowDropDown';
import CancelIcon from '@material-ui/icons/Cancel';
import ArrowDropUpIcon from '@material-ui/icons/ArrowDropUp';
import ClearIcon from '@material-ui/icons/Clear';
import Chip from '@material-ui/core/Chip';
import Select from 'react-select';
import Button from '@material-ui/core/Button';
import Slider from 'rc-slider';
import blue from '@material-ui/core/colors/blue';
import texts from '../../services/texts/index';
import countYears from './countYears.js';
import ApiService from './../../services/api';
import config from './../../configs';
import serialize from './../../services/serialize';

const ITEM_HEIGHT = 48;
const OLDEST_CARS = 30;
const years = countYears(OLDEST_CARS);
const startYear = years[0].value;
const endYear = years[years.length - 1].value;

const manufacturers = [
  { value: 'Toyota',label: 'Toyota' },
  { value: 'Ford',label: 'Ford' },
  { value: 'Chevrolet',label: 'Chevrolet' },
  { value: 'Nissan',label: 'Nissan' },
  { value: 'Hyundai',label: 'Hyundai' },
  { value: 'KIA',label: 'KIA' },
  { value: 'Daewoo',label: 'Daewoo' },
  { value: 'Peugeot',label: 'Peugeot' },
  { value: 'УАЗ',label: 'УАЗ' },
  { value: 'LADA',label: 'LADA' },
  { value: 'jeep',label: 'jeep' },
  { value: 'Subaru',label: 'Subaru' },
  { value: 'Lexus',label: 'Lexus' },
  { value: 'Suzuki',label: 'Suzuki' },
  { value: 'Mitsubishi',label: 'Mitsubishi' },
  { value: 'Volvo',label: 'Volvo' },
];
const resultCars = [
  {
    img: 'https://cdn2.riastatic.com/photosnew/auto/photo/tesla_model-s__236718267bx.jpg',
    name: 'Tesla Model S 70D 2015',
    place: 'Харьков',
    price: '51 000 $',
    millage: '18 000',
    engine: 'Электро',
    transmission: 'Автомат',
    description: 'Отличное состояние. пробег 17 тыс км. салон кожа, потолок алькантара, торпедо кожа/алькантара. есть все кроме пневмо подвески и панарамной крыши. резина летняя и зимняя новая.',
    date: '08.06.2018'
  },{
    img: 'https://cdn4.riastatic.com/photosnew/auto/photo/tesla_model-s__212678044bx.jpg',
    name: 'Tesla Model S Brabus Performance 2017',
    place: 'Киев',
    price: '160 100 $',
    millage: 'без пробега',
    engine: 'Электро',
    transmission: 'Автомат',
    description: 'Тesla s (performance) рестайлинг brabus 2017г - сидения ,коврики brabus, 762л.с. - полный привод, 2,9 сек до 100 км - стеклянная крыша понорама - художественное оформление салона лак',
    date: '22.06.2018'
  },{
    img: 'https://cdn4.riastatic.com/photosnew/auto/photo/mitsubishi_l-200__240849404f.jpg',
    name: 'Tesla Model S Brabus Performance 2017',
    place: 'Киев',
    price: '160 100 $',
    millage: 'без пробега',
    engine: 'Электро',
    transmission: 'Автомат',
    description: 'Тesla s (performance) рестайлинг brabus 2017г - сидения ,коврики brabus, 762л.с. - полный привод, 2,9 сек до 100 км - стеклянная крыша понорама - художественное оформление салона лак',
    date: '22.06.2018'
  },{
    img: 'https://cdn0.riastatic.com/photosnew/auto/photo/nissan_leaf__233583805b.jpg',
    name: 'Tesla Model S Brabus Performance 2017',
    place: 'Киев',
    price: '160 100 $',
    millage: 'без пробега',
    engine: 'Электро',
    transmission: 'Автомат',
    description: 'Тesla s (performance) рестайлинг brabus 2017г - сидения ,коврики brabus, 762л.с. - полный привод, 2,9 сек до 100 км - стеклянная крыша понорама - художественное оформление салона лак',
    date: '22.06.2018'
  },{
    img: 'https://cdn3.riastatic.com/photosnew/auto/photo/zaz_sens__240197818bx.jpg',
    name: 'Tesla Model S Brabus Performance 2017',
    place: 'Киев',
    price: '160 100 $',
    millage: 'без пробега',
    engine: 'Электро',
    transmission: 'Автомат',
    description: 'Тesla s (performance) рестайлинг brabus 2017г - сидения ,коврики brabus, 762л.с. - полный привод, 2,9 сек до 100 км - стеклянная крыша понорама - художественное оформление салона лак',
    date: '22.06.2018'
  }
];

const styles = (theme) => ({
  mileageField: {
    width: '100%',
    marginTop: 0
  },
  subheading: {
    textAlign: 'left',
    minHeight: 24
  },
  button: {
    width: '100%'
  },
  textField: {
    width: '100%',
  },
  paperRelative: {
    position: 'relative',
  },
  milesLabel: {
    position: 'absolute',
    bottom: 25,
    right: 20
  },
  chip: {
    margin: theme.spacing.unit / 4,
  },
  paper: {
    padding: 15,
    marginTop: 10,
    borderRadius: 0,
    color: theme.palette.text.secondary,
    boxShadow: 'none',
    textAlign: 'center'
  },
  '@global': {
    '#root': {
      overflow: 'hidden'
    },
    '.rc-slider-handle': {
      border: `2px solid ${blue[600]}`,
      marginTop: -8,
      marginLeft: -10,
      width: 20,
      height: 20
    },
    '.rc-slider-handle:active': {
      borderColor: blue[100],
      boxShadow: `0 0 5px ${blue[600]}`
    },
    '.rc-slider-track': {
      backgroundColor: blue[600]
    },
    '.Select-control': {
      display: 'flex',
      alignItems: 'center',
      border: 0,
      height: 'auto',
      background: 'transparent',
      '&:hover': {
        boxShadow: 'none',
      },
    },
    '.Select-multi-value-wrapper': {
      flexGrow: 1,
      display: 'flex',
      flexWrap: 'wrap',
    },
    '.Select--multi .Select-input': {
      margin: 0,
    },
    '.Select.has-value.is-clearable.Select--single > .Select-control .Select-value': {
      padding: 0,
    },
    '.Select-noresults': {
      padding: theme.spacing.unit * 2,
    },
    '.Select-input': {
      display: 'inline-flex !important',
      padding: 0,
      height: 'auto',
    },
    '.Select-input input': {
      background: 'transparent',
      border: 0,
      padding: 0,
      cursor: 'default',
      display: 'inline-block',
      fontFamily: 'inherit',
      fontSize: 'inherit',
      margin: 0,
      outline: 0,
    },
    '.Select-placeholder, .Select--single .Select-value': {
      position: 'absolute',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      display: 'flex',
      alignItems: 'center',
      fontFamily: theme.typography.fontFamily,
      fontSize: theme.typography.pxToRem(16),
      padding: 0,
    },
    '.Select-placeholder': {
      opacity: 0.42,
      color: theme.palette.common.black,
    },
    '.Select-menu-outer': {
      backgroundColor: theme.palette.background.paper,
      boxShadow: theme.shadows[2],
      position: 'absolute',
      left: 0,
      top: `calc(100% + ${theme.spacing.unit}px)`,
      width: '100%',
      zIndex: 2,
      maxHeight: ITEM_HEIGHT * 4.5,
    },
    '.Select.is-focused:not(.is-open) > .Select-control': {
      boxShadow: 'none',
    },
    '.Select-menu': {
      maxHeight: ITEM_HEIGHT * 4.5,
      overflowY: 'auto',
    },
    '.Select-menu div': {
      boxSizing: 'content-box',
    },
    '.Select-arrow-zone, .Select-clear-zone': {
      color: theme.palette.action.active,
      cursor: 'pointer',
      height: 21,
      width: 21,
      zIndex: 1,
    },
    '.Select-aria-only': {
      position: 'absolute',
      overflow: 'hidden',
      clip: 'rect(0 0 0 0)',
      height: 1,
      width: 1,
      margin: -1,
    },
  },
});

const createSliderWithTooltip = Slider.createSliderWithTooltip;
const Range = createSliderWithTooltip(Slider.Range);

class Option extends Component {
  handleClick = event => {
    this.props.onSelect(this.props.option, event);
  };
  render() {
    const { children, isFocused, isSelected, onFocus } = this.props;
    return (
      <MenuItem
        onFocus={onFocus}
        selected={isFocused}
        onClick={this.handleClick}
        component='div'
        style={{
          fontWeight: isSelected ? 500 : 400,
        }}>
        {children}
      </MenuItem>
    );
  }
}

function SelectWrapped(props) {
  const { classes, ...other } = props;
  return (
    <Select
      optionComponent={Option}
      noResultsText={<Typography>{'No results found'}</Typography>}
      arrowRenderer={arrowProps => {
        return arrowProps.isOpen ? <ArrowDropUpIcon /> : <ArrowDropDownIcon />;
      }}
      clearRenderer={() => <ClearIcon />}
      valueComponent={valueProps => {
        const { value, children, onRemove } = valueProps;
        const onDelete = event => {
          event.preventDefault();
          event.stopPropagation();
          onRemove(value);
        };
        if (onRemove) {
          return (
            <Chip
              tabIndex={-1}
              label={children}
              className={classes.chip}
              deleteIcon={<CancelIcon onTouchEnd={onDelete} />}
              onDelete={onDelete}
            />
          );
        }
        return <div className='Select-value'>{children}</div>;
      }}
      {...other}
    />
  );
}

class Form extends Component {

  constructor(props) {
    super(props);
    this.config = config();
    this.state = {
      years: null,
      manufacturers: null,
      models: null,
      manufacturer: '',
      model: '',
      mileage_min: 0,
      mileage_max: 100,
      year_min: startYear,
      year_max: endYear
    };
  }

  handleChange = name => value => {
    this.setState({
      [name]: value
    });
  };

  handleMillageChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value
    });
  };

  handleRangeYearsChange = (value) => {
    this.setState({
      year_min: value[0],
      year_max: value[1]
    });
  };

  checkValues = (val1,val2,type) => {
    let valuesArray =  ( val1 > val2 ? [val2,val1] : [val1,val2] );
    this.setState({
      [`selected${type}Min`]: Number(valuesArray[0]),
      [`selected${type}Max`]: Number(valuesArray[1])
    });
    return valuesArray;
  };

  submitForm = () => {
    const searchParams = serialize(this.searchForm);
    const apiService = new ApiService();
    apiService.postRequest(this.config.snoops,searchParams)
      .then((result)=>{
        console.log(result);
      }).catch(()=>{
    });
    setTimeout( () => {
      this.props.submitForm(resultCars);
    },1000);
  };

  render() {
    const {classes} = this.props;
    const {year_min,year_max} = this.state;
    const rangeValue = [year_min, year_max];
    return (
      <Grid className={classes.grid} item lg={3} md={4} sm={4} xs={11}>
        <Paper className={classes.paper}>
          <form
            noValidate
            autoComplete='off'
            ref={(ref) => { this.searchForm = ref; }}
          >
            <Grid
              container
              spacing={24}
              justify='center'
              direction='row'
            >
              <Grid className={classes.paperRelative} item lg={12} md={12} sm={12} xs={12}>
                <Typography className={classes.subheading} variant='subheading'>
                  {texts.texts.manufacturer}
                </Typography>
                <Input
                  fullWidth
                  inputComponent={SelectWrapped}
                  placeholder={texts.texts.manufacturer}
                  inputProps={{
                    classes,
                    name: 'manufacturer',
                    instanceId: 'manufacturer',
                    simpleValue: true,
                    options: manufacturers,
                  }}
                  value={this.state.manufacturer}
                  onChange={this.handleChange('manufacturer')}
                />
              </Grid>
            </Grid>
            <Grid
              container
              spacing={24}
              justify='center'
              direction='row'
            >
              <Grid className={classes.paperRelative} item lg={12} md={12} sm={12} xs={12}>
                <Typography className={classes.subheading} variant='subheading'>
                  {texts.texts.model}
                </Typography>
                <Input
                  fullWidth
                  inputComponent={SelectWrapped}
                  placeholder={texts.texts.model}
                  inputProps={{
                    classes,
                    name: 'model',
                    instanceId: 'model',
                    simpleValue: true,
                    options: manufacturers,
                  }}
                  value={this.state.model}
                  onChange={this.handleChange('model')}
                />
              </Grid>
            </Grid>
            <Grid
              container
              spacing={24}
              justify='center'
              direction='row'
            >
              <Grid className={classes.paperRelative} item lg={6} md={6} sm={6} xs={6}>
                <Typography className={classes.subheading} variant='subheading'>
                  {texts.texts.year}
                </Typography>
                <Input
                  fullWidth
                  inputComponent={SelectWrapped}
                  name='year_min'
                  placeholder={texts.texts.yearMin}
                  inputProps={{
                    classes,
                    name: 'year_min',
                    instanceId: 'year_min',
                    simpleValue: true,
                    options: years,
                  }}
                  value={this.state.year_min}
                  onChange={this.handleChange('year_min')}
                />
              </Grid>
              <Grid className={classes.paperRelative} item lg={6} md={6} sm={6} xs={6}>
                <Typography className={classes.subheading} variant='subheading'>
                </Typography>
                <Input
                  fullWidth
                  inputComponent={SelectWrapped}
                  name='year_max'
                  placeholder={texts.texts.yearMax}
                  inputProps={{
                    classes,
                    name: 'year_max',
                    instanceId: 'year_max',
                    simpleValue: true,
                    options: years,
                  }}
                  value={this.state.year_max}
                  onChange={this.handleChange('year_max')}
                />
              </Grid>
              <Grid className={classes.paperRelative} item lg={12} md={12} sm={12} xs={12}>
                <Range
                  onChange={this.handleRangeYearsChange}
                  min={startYear}
                  max={endYear}
                  value={rangeValue}
                  tipFormatter={value => `${value}`}
                />
              </Grid>
            </Grid>
            <Grid
              container
              spacing={24}
              justify='center'
              direction='row'>
              <Grid className={classes.paperRelative} item lg={6} md={6} sm={6} xs={6}>
                <Typography className={classes.subheading} variant='subheading'>
                  {texts.texts.mileage}
                </Typography>
                <TextField
                  type='number'
                  id='mileage_min'
                  name='mileage_min'
                  label={texts.texts.km}
                  className={classes.mileageField}
                  onChange={this.handleMillageChange}
                  value={this.state.mileage_min}
                />
              </Grid>
              <Grid className={classes.paperRelative} item lg={6} md={6} sm={6} xs={6}>
                <Typography className={classes.subheading} variant='subheading'>
                </Typography>
                <TextField
                  type='number'
                  id='mileage_max'
                  name='mileage_max'
                  label={texts.texts.km}
                  className={classes.mileageField}
                  onChange={this.handleMillageChange}
                  value={this.state.mileage_max}
                />
              </Grid>
            </Grid>
            <Grid
              container
              spacing={24}
              justify='center'
              direction='row'>
              <Grid className={classes.paperRelative} item lg={12} md={12} sm={12} xs={12}>
                <Button
                  onClick = {this.submitForm}
                  variant='contained'
                  color='primary'
                  className={classes.button}
                >
                  {texts.texts.createSnoop}
                </Button>
              </Grid>
            </Grid>
          </form>
        </Paper>
      </Grid>
    );
  }
}

export default withStyles(styles)(Form);